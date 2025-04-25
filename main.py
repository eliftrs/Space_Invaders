print("Merhaba GitHub! Bugünkü katkı testi ✅")
print("Uzaylılar saldırıyor!")
score = 0

def update_score(points):
    global score
    score += points
    print(f"Skor: {score}")

# test
update_score(10)
update_score(5)

print("Oyun başlıyor...")
print("=== SPACE INVADERS ===")
def update_score(score):
    score += 10
    print(f"Skor: {score}")
    return score
enemy_speed = 1.0  # Düşman hızı
