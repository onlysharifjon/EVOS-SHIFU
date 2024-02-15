import sqlite3

connect = sqlite3.connect('evos_.database.db')
cursor = connect.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS mahsulotlar(name TEXT,price INTEGR,image TEXT,category TEXT)")
#
#
# #
# a = ["Shaurma qalampir mol go'sht;22000;Shaurma_qalampir_mol_gosht.jpg",
#      "Shaurma tovuq go'sht;24000;Shaurma_tovuq_gosht.jpg",
#      "Shaurma qalampir tovuq go'sht;26000;Shaurma_qalampir_tovuq_gosht.jpg",
#      "Shaurma mol go'sht;24000;Shaurma_mol_gosht.jpg",
#      "Gamburger;22000;Gamburger.jpg",
#      "Double burger;33000;Double_burger.jpg",
#      "Cheese burger;24000;Cheese_burger.jpg",
#      "Double cheese;37000;Double_cheese.jpg",
#      ]
# mahsulot_nomi = ['Combo Plus Isituvchan (Qora choy)', 'FitCombo', "Iftar kofte grill mol go'shtidan",
#                  "Donar boks  mol go'shtidan", "Donar boks tovuq go'shtidan", 'COMBO+', "Iftar strips tovuq go'shtidan",
#                  'Kids COMBO', 'Mol goʼshtidan qalampir lavash', 'Tovuq goʼshtli qalampir lavash',
#                  "Mol go'shtidan pishloqli lavash Standard", "Lavash cheese tovuq go'sht Standart", 'FITTER',
#                  "Lavash tovuq go'sht", "Lavash mol go'sht"]
# narxlar = [28000, 25000, 27000, 24000, 28000, 25000, 24000, 24000, 26000, 24000, 29000, 29000, 22000, 24000, 26000]
#
# rasmlar = ['ComboPlusIsituvchan(Qora choy).jpg', 'Fit_Combo.jpg', 'Iftar_kofte_grill_mol_goshtidan.jpg',
#            'Donar_boks_mol_goshtidan.jpg', 'Donar_boks_tovuq_goshtidan.jpg', 'COMBO+.jpg',
#            'Iftar_strips_tovuq_goshtidan.jpg', 'Kids_COMBO.jpg', 'Mol_goshtidan_qalampir_lavash.jpg',
#            'Tovuq_goshtli_qalampir_lavash.jpg', 'Mol_goshtidan_pishloqli_lavash_standard.jpg',
#            'Lavash_cheese_tovuq_gosht_standart.jpg', 'FITTER.jpg', 'Lavash_tovuq_gosht.jpg', 'Lavash_mol_gosht.jpg']
#
# bolimlar = ['setlar', 'setlar', 'setlar', 'setlar', 'setlar', 'setlar', 'setlar', 'setlar', 'lavashlar', 'lavashlar',
#             'lavashlar', 'lavashlar', 'lavashlar', 'lavashlar', 'lavashlar']


cursor.execute('INSERT INTO mahsulotlar VALUES (?,?,?,?)',
               (f"Fri", 14000, f"Fri.jpg", f'garnirlar'))


connect.commit()