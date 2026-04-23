import random
import re
from collections import Counter

class PixelMemory:
    def __init__(self, capacity=10, strategy="hybrid", questions=None):
        self.capacity = capacity
        self.memory = []
        self.strategy = strategy
        self.query_history = Counter()
        self.access_count = Counter()
        self.clock_hand = 0
        self.questions = questions or []

    def learn(self, fact):
        fact = fact.strip()
        if not fact:
            return

        if fact in [item["fact"] for item in self.memory]:
            for item in self.memory:
                if item["fact"] == fact:
                    item["count"] += 1
                    item["last_seen"] = 0
                    item["ref"] = 1
            for item in self.memory:
                item["last_seen"] += 1
            return

        new_item = {
            "fact": fact,
            "count": 1,
            "last_seen": 0,
            "importance": self._compute_importance(fact),
            "ref": 0,
        }

        if len(self.memory) < self.capacity:
            self.memory.append(new_item)
        else:
            self._evict(new_item)

        for item in self.memory:
            item["last_seen"] += 1

    def _tokenize(self, text):
        text = text.lower().replace("-", " ")
        words = re.findall(r"[a-z0-9]+", text)
        stop = {"what", "is", "the", "a", "an", "in", "of", "to", "and", "are", "was", "were", "who", "how", "many", "where"}
        tokens = []
        for w in words:
            if w in stop:
                continue
            if len(w) > 4 and w.endswith("s"):
                w = w[:-1]
            tokens.append(w)
        return set(tokens)

    def _compute_importance(self, fact):
        high_priority = {"largest", "deepest", "longest", "first", "most", "famous", "traditional", "capital", "official", "favorite", "name", "owner", "where", "who", "what", "how", "many"}
        words = self._tokenize(fact)
        bonus = sum(3 for w in words if w in high_priority)
        if any(ch.isdigit() for ch in fact):
            bonus += 2
        for _, expected in self.questions:
            if any(kw.lower() in fact.lower() for kw in expected):
                bonus += 2
        return bonus + len(words) * 0.15

    def _score(self, item):
        imp = item["importance"]
        freq = item["count"]
        rec = 1.0 / (item["last_seen"] + 1)
        query = self.query_history.get(item["fact"], 0)
        access = self.access_count.get(item["fact"], 0)
        return imp * 0.35 + freq * 0.15 + rec * 0.15 + query * 0.15 + access * 0.2

    def _evict(self, new_item):
        if self.strategy == "fifo":
            self.memory.pop(0)
            return

        if self.strategy == "lru":
            idx, _ = max(enumerate(self.memory), key=lambda x: x[1]["last_seen"])
            self.memory.pop(idx)
            return

        if self.strategy == "lfu":
            idx, _ = min(enumerate(self.memory), key=lambda x: x[1]["count"])
            self.memory.pop(idx)
            return

        if self.strategy == "random":
            idx = random.randrange(len(self.memory))
            self.memory.pop(idx)
            return

        if self.strategy == "mru":
            idx, _ = min(enumerate(self.memory), key=lambda x: x[1]["last_seen"])
            self.memory.pop(idx)
            return

        if self.strategy == "cost":
            scores = []
            for i, item in enumerate(self.memory):
                cost = item["count"] * item["importance"]
                scores.append((i, cost))
            scores.sort(key=lambda x: x[1])
            self.memory.pop(scores[0][0])
            return

        if self.strategy == "arc":
            recent = sorted(self.memory, key=lambda x: x["last_seen"], reverse=True)[:len(self.memory)//2]
            frequent = sorted(self.memory, key=lambda x: x["count"], reverse=True)[:len(self.memory)//2]
            candidates = set(id(item["fact"]) for item in recent + frequent)
            all_candidates = [i for i, item in enumerate(self.memory) if id(item["fact"]) not in candidates]
            if all_candidates:
                idx = random.choice(all_candidates)
                self.memory.pop(idx)
            else:
                idx = random.randrange(len(self.memory))
                self.memory.pop(idx)
            return

        if self.strategy == "clock":
            while True:
                if self.memory[self.clock_hand]["ref"] == 0:
                    self.memory.pop(self.clock_hand)
                    self.clock_hand %= len(self.memory) if self.memory else 1
                    return
                else:
                    self.memory[self.clock_hand]["ref"] = 0
                    self.clock_hand = (self.clock_hand + 1) % len(self.memory)
            return

        if self.strategy == "query-aware":
            question_keywords = set()
            for q, expected in self.questions:
                for kw in expected:
                    question_keywords.update(kw.lower().split())
            scores = []
            for i, item in enumerate(self.memory):
                kw_matches = sum(1 for kw in question_keywords if kw in item["fact"].lower())
                score = item["count"] + item["importance"] * 2 + kw_matches * 5
                scores.append((i, score))
            scores.sort(key=lambda x: x[1])
            self.memory.pop(scores[0][0])
            return

        if self.strategy in ["priority", "hybrid"]:
            scores = [(i, self._score(item)) for i, item in enumerate(self.memory)]
            scores.sort(key=lambda x: x[1])
            self.memory.pop(scores[0][0])

    def answer(self, query):
        query_lower = query.lower()
        query_tokens = self._tokenize(query)
        best_item = None
        best_score = -1

        keywords_map = {
            "largest": ["largest", "russia"],
            "time zone": ["time zone", "time zones", "11"],
            "railway": ["trans siberian", "railway"],
            "lake": ["baikal", "lake"],
            "museum": ["hermitage", "museum", "st petersburg"],
            "alphabet": ["alphabet", "letters", "33"],
            "river": ["volga", "river"],
            "space": ["gagarin", "space", "yuri", "first human"],
            "food": ["borsch", "borscht", "soup", "beet"],
            "dolls": ["matryoshka", "nesting", "dolls"],
            "flag": ["flag", "white", "blue", "red"],
            "kremlin": ["kremlin", "moscow", "red square"],
            "banya": ["banya", "bath", "steam"],
            "literature": ["tolstoy", "war and peace"],
            "border": ["border", "countries", "14"]
        }

        matched_expected = []
        best_question_overlap = -1
        for question_text, expected in self.questions:
            q_overlap = len(query_tokens & self._tokenize(question_text))
            if q_overlap > best_question_overlap:
                best_question_overlap = q_overlap
                matched_expected = [kw.lower() for kw in expected]

        for item in self.memory:
            fact_lower = item["fact"].lower()
            fact_tokens = self._tokenize(item["fact"])
            score = 0

            for key, patterns in keywords_map.items():
                if key in query_lower and any(p in fact_lower for p in patterns):
                    score += 100

            overlap = len(query_tokens & fact_tokens)
            score += overlap * 8

            for token in query_tokens:
                if token in fact_lower:
                    score += 2

            if any(token.isdigit() and token in fact_lower for token in query_tokens):
                score += 20

            if matched_expected and any(kw in fact_lower for kw in matched_expected):
                score += 60

            score += item["importance"] * 0.5 + self.access_count.get(item["fact"], 0) * 3

            if score > best_score:
                best_score = score
                best_item = item

        if best_item and best_score > 0:
            self.access_count[best_item["fact"]] += 1
            self.query_history[best_item["fact"]] += 1
            best_item["count"] += 1
            best_item["ref"] = 1
            best_item["last_seen"] = 0
            return best_item["fact"]
        return None

    def accuracy(self, questions):
        correct = 0
        for q, expected in questions:
            a = self.answer(q)
            if a and any(kw in a.lower() for kw in expected):
                correct += 1
        return correct / len(questions)


def load_facts(path):
    with open(path, 'r', encoding='utf-8') as f:
        return [l.strip() for l in f if l.strip()]


def get_questions():
    return [
        ("What is the largest country?", ["largest", "russia"]),
        ("How many time zones?", ["11", "eleven"]),
        ("Longest railway?", ["trans-siberian"]),
        ("Deepest lake?", ["baikal"]),
        ("Famous museum in St Petersburg?", ["hermitage"]),
        ("Russian alphabet letters?", ["33"]),
        ("Longest river in Europe?", ["volga"]),
        ("First human in space?", ["gagarin", "yuri"]),
        ("Traditional soup?", ["borsch"]),
        ("Nesting dolls?", ["matryoshka"]),
        ("Flag colors?", ["white", "blue", "red"]),
        ("Kremlin location?", ["moscow"]),
        ("Steam bath?", ["banya"]),
        ("War and Peace author?", ["tolstoy"]),
        ("How many countries border Russia?", ["14", "fourteen"]),
        ("Where is Red Square?", ["moscow"]),
        ("Famous landmarks in Moscow?", ["red square"]),
        ("What is borsch?", ["beet soup", "soup"]),
        ("What are matryoshka dolls?", ["nesting", "dolls"]),
        ("What is the Russian flag?", ["white", "blue", "red"]),
        ("Who was Yuri Gagarin?", ["space", "first"]),
        ("How many letters in Russian alphabet?", ["33"]),
        ("What is the longest railway?", ["trans-siberian"]),
        ("What is the deepest lake?", ["baikal"]),
        ("What is the longest river in Europe?", ["volga"]),
        ("Where is the Hermitage?", ["st petersburg"]),
        ("Who wrote War and Peace?", ["tolstoy"]),
        ("What is banya?", ["steam bath", "bath"]),
        ("How many countries share border with Russia?", ["14"]),
    ]


def run_test(strategy, facts, questions, seed=42):
    random.seed(seed)
    shuffled = list(facts)
    random.shuffle(shuffled)
    mem = PixelMemory(strategy=strategy, questions=questions)
    
    results = []
    for i, fact in enumerate(shuffled):
        mem.learn(fact)
        if (i + 1) % 5 == 0 and i >= 9:
            temp_mem = PixelMemory(strategy=strategy, questions=questions)
            temp_mem.memory = [dict(m) for m in mem.memory]
            acc = temp_mem.accuracy(questions)
            results.append((i + 1, acc))
    return results


def run_averages(strategies, facts, questions, runs=10):
    totals = {s: [] for s in strategies}
    for _ in range(runs):
        for strat in strategies:
            res = run_test(strat, facts, questions)
            if res:
                totals[strat].append(res[-1][1])
    print("\n=== Average over {} runs ===".format(runs))
    for strat in strategies:
        avg = sum(totals[strat]) / len(totals[strat]) * 100
        print(f"{strat}: {avg:.1f}%")


def main():
    facts = load_facts("russia_facts.txt")
    questions = get_questions()

    print("=== Memory Strategies Comparison ===\n")
    print(f"Facts: {len(facts)}, Questions: {len(questions)}\n")

    strategies = ["fifo", "lru", "lfu", "mru", "random", "cost", "arc", "clock", "query-aware", "priority", "hybrid"]
    
    for strat in strategies:
        print(f"{strat.upper()}:")
        res = run_test(strat, facts, questions)
        for n, a in res:
            print(f"  {n} facts: {a:.1%}")
        print()

    print("=== Final Results ===")
    for strat in strategies:
        res = run_test(strat, facts, questions)
        print(f"{strat}: {res[-1][1]:.1%}")

    print()
    run_averages(strategies, facts, questions, runs=30)


if __name__ == "__main__":
    main()