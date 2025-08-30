# dev_elma_ascii.py
width = 200      # Genişlik (karakter sayısı)
height = 100     # Yükseklik (satır sayısı)
output_file = "dev_elma.txt"

apple = []

for y in range(height):
    line = ""
    for x in range(width):
        # Elmanın yuvarlak şekli için denklem
        dx = (x - width / 2) / (width / 2)
        dy = (y - height / 2) / (height / 2)
        distance = dx*dx + dy*dy

        if distance <= 0.25:  # Elma içi
            line += "@"
        elif distance <= 0.27:  # Elma kenarı
            line += "#"
        else:
            line += " "
    apple.append(line)

# Sap ekleyelim
for i in range(5):
    sap_line = " " * (width//2) + "||"
    apple.insert(0, sap_line)

# Yaprak ekleyelim
leaf_line = " " * (width//2 - 5) + "/\\"
apple.insert(0, leaf_line)

# Dosyaya yaz
with open(output_file, "w", encoding="utf-8") as f:
    for line in apple:
        f.write(line + "\n")

print(f"Dev elma ASCII'si {output_file} dosyasına yazıldı!")
