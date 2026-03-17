import random
from rich.console import Console
from rich.table import Table

def simulate_loot(chests=10):
    loot_types = ["Common", "Rare", "Epic", "Legendary"]
    probabilities = [0.7, 0.2, 0.08, 0.02]
    results = {loot: 0 for loot in loot_types}

    for _ in range(chests):
        loot = random.choices(loot_types, probabilities)[0]
        results[loot] += 1

    console = Console()
    table = Table(title="LootGen — Результаты")
    table.add_column("Тип лута")
    table.add_column("Количество")
    for loot_type, count in results.items():
        table.add_row(loot_type, str(count))
    console.print(table)

if __name__ == "__main__":
    simulate_loot(20)
