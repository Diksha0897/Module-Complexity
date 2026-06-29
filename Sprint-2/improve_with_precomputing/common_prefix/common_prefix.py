from typing import List, Dict


class TrieNode:
    __slots__ = ("children", "count")

    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.count = 0


def find_longest_common_prefix(strings: List[str]) -> str:
    if len(strings) < 2:
        return ""

    root = TrieNode()

    # ---- PRECOMPUTE: build trie ----
    for s in strings:
        node = root
        for ch in s:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count += 1

    # ---- FIND BEST PREFIX ----
    best_prefix = []
    node = root

    while True:
        # pick a child that still has at least 2 strings passing through
        next_node = None
        next_char = None

        for ch, child in node.children.items():
            if child.count >= 2:
                next_node = child
                next_char = ch
                break

        if not next_node:
            break

        best_prefix.append(next_char)
        node = next_node

    return "".join(best_prefix)
