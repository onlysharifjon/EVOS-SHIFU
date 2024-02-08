# import sqlite3
#
# connect = sqlite3.connect('evos_.database.db')
# cursor = connect.cursor()
#
# cursor.execute("CREATE TABLE IF NOT EXISTS mahsulotlar(name TEXT,price INTEGR,image TEXT,category TEXT)")
# cursor.execute('INSERT INTO mahsulotlar VALUES (?,?,?,?)',
#                ("Lavash mol go'sht", 26000, "Lavash_mol_gosht.jpg", 'lavashlar'))
# connect.commit()
# #
a = ["Combo Plus Isituvchan (Qora choy);28000;ComboPlusIsituvchan(Qora choy).jpg;setlar",
     "FitCombo;25000;Fit_Combo.jpg;setlar",
     "Iftar kofte grill mol go'shtidan;27000;Iftar_kofte_grill_mol_goshtidan.jpg;setlar",
     "Donar boks  mol go'shtidan;24000;Donar_boks_mol_goshtidan.jpg;setlar",
     "Donar boks tovuq go'shtidan;28000;Donar_boks_tovuq_goshtidan.jpg;setlar",
     "COMBO+;25000;COMBO+.jpg;setlar",
     "Iftar strips tovuq go'shtidan;24000;Iftar_strips_tovuq_goshtidan.jpg;setlar",
     "Kids COMBO;24000;Kids_COMBO.jpg;setlar",
     "Mol goʼshtidan qalampir lavash;26000;Mol_goshtidan_qalampir_lavash.jpg;lavashlar",
     "Tovuq goʼshtli qalampir lavash;24000;Tovuq_goshtli_qalampir_lavash.jpg;lavashlar",
     "Mol go'shtidan pishloqli lavash Standard;29000;Mol_goshtidan_pishloqli_lavash_standard.jpg;lavashlar",
     "Lavash cheese tovuq go'sht Standart;29000;Lavash_cheese_tovuq_gosht_standart.jpg;lavashlar",
     "FITTER;22000;FITTER.jpg;lavashlar",
     "Lavash tovuq go'sht;24000;Lavash_tovuq_gosht.jpg;lavashlar",
     "Lavash mol go'sht;26000;Lavash_mol_gosht.jpg;lavashlar"]
mahsulot_nomi = ['Combo Plus Isituvchan (Qora choy)', 'FitCombo', "Iftar kofte grill mol go'shtidan",
                 "Donar boks  mol go'shtidan", "Donar boks tovuq go'shtidan", 'COMBO+', "Iftar strips tovuq go'shtidan",
                 'Kids COMBO', 'Mol goʼshtidan qalampir lavash', 'Tovuq goʼshtli qalampir lavash',
                 "Mol go'shtidan pishloqli lavash Standard", "Lavash cheese tovuq go'sht Standart", 'FITTER',
                 "Lavash tovuq go'sht", "Lavash mol go'sht"]
narxlar = [28000, 25000, 27000, 24000, 28000, 25000, 24000, 24000, 26000, 24000, 29000, 29000, 22000, 24000, 26000]
rasmlar =  ['ComboPlusIsituvchan(Qora choy).jpg', 'Fit_Combo.jpg', 'Iftar_kofte_grill_mol_goshtidan.jpg', 'Donar_boks_mol_goshtidan.jpg', 'Donar_boks_tovuq_goshtidan.jpg', 'COMBO+.jpg', 'Iftar_strips_tovuq_goshtidan.jpg', 'Kids_COMBO.jpg', 'Mol_goshtidan_qalampir_lavash.jpg', 'Tovuq_goshtli_qalampir_lavash.jpg', 'Mol_goshtidan_pishloqli_lavash_standard.jpg', 'Lavash_cheese_tovuq_gosht_standart.jpg', 'FITTER.jpg', 'Lavash_tovuq_gosht.jpg', 'Lavash_mol_gosht.jpg']

for i in a:
    txt = ''
    cnt = 0
    for harf in i:
        if harf == ';':
            cnt += 1
        if cnt == 3:
            id = txt.rfind(';')
            rasmlar.append(txt[id + 1::])

            break
        txt += harf

print(f"rasmlar = ", rasmlar)
