# Valutaomregner CLI

Et simpelt command line tool til valutaomregning via [ExchangeRate API](https://www.exchangerate-api.com/).

---

## Krav

- Python 3.8+
- En gratis API nøgle fra [exchangerate-api.com](https://www.exchangerate-api.com/)

---

## Installation

### 1. Klon projektet

```bash
git clone https://github.com/dit-brugernavn/dit-repo.git
cd dit-repo
```

### 2. Opret virtuelt miljø

```bash
python3 -m venv .venv
```

### 3. Aktiver virtuelt miljø

**Mac/Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### 4. Installer dependencies
´´bash
uv sync
´´


```bash
pip install -r requirements.txt
```

---

## Brug

### Første gang — tilføj din API nøgle

```bash
python3 valuta.py --key DIN_API_NØGLE
```

Dette gemmer nøglen i en `.env` fil, så du ikke behøver at indtaste den igen.

### Efterfølgende gange

```bash
python3 valuta.py
```

Programmet guider dig igennem resten:

```
Indtast første valuta: DKK
Indtast anden valuta: EUR
Indtast hvad du vil veksle: 100

Conversion rate: 0.134
Result: 13.4
```

---

## Deaktiver virtuelt miljø

Når du er færdig kan du deaktivere det virtuelle miljø med:

```bash
deactivate
```
