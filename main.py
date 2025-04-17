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

