**Generare Oferte AI**

**Descriere**

Acest proiect descarcă, pregătește și antrenează un model AI pentru a genera oferte pe baza datelor furnizate. Utilizează modele pre-antrenate GPT-2 pentru a procesa exemple de oferte și a crea noi oferte în funcție de cerințele clienților.

**Cerințe**

- Python 3.x
- Pachete necesare (instalate prin pip):
  - `requests`
  - `transformers`
  - `torch`
  - `datasets`
  - `python-docx`

**Instalare**

1. Clonează repository-ul:
   ```bash
   git clone https://github.com/numele_tău/Generare_Oferte.git
   cd Generare_Oferte

2. Instalează dependențele:
pip install requests transformers torch datasets python-docx

**Utilizare**

1. Descărcarea și extragerea arhivei
Rulează scriptul pentru a descărca și extrage arhiva:
python download_and_extract.py

2. Descărcarea și salvarea modelului pre-antrenat
Rulează scriptul pentru a descărca și salva modelul pre-antrenat:
python download_and_save_model.py

3. Pregătirea datelor pentru antrenament
Rulează scriptul pentru a pregăti datele din fișierele .docx:
python prepare_data.py

4. Antrenarea modelului
Rulează scriptul pentru a antrena modelul:
python train_model.py

5. Generarea ofertelor
Rulează scriptul pentru a genera oferte pe baza inputului dat:
python generate.py
