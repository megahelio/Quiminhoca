# 🔬 Chemical Formula Lookup API

API para consultar información química pública a partir de fórmulas moleculares simples, con soporte para múltiples fuentes (actualmente PubChem). Ideal como punto de partida para sistemas de interpretación de datos provenientes de instrumentos como espectrómetros de masas o cromatógrafos.

---

## 🚀 ¿Qué hace?

Dada una fórmula química (ej. `C6H12O6`), esta API:

- Busca compuestos coincidentes en bases de datos públicas (empezando por **PubChem**)
- Devuelve información como:
  - Nombre IUPAC
  - Fórmula molecular
  - Peso molecular
- Utiliza **Redis** como caché para evitar consultas repetidas

---

## 🛠️ Requisitos

- Python 3.12.1
- Docker (opcional, para Redis)
- Redis ejecutándose localmente

---

## ⚙️ Instalación

```bash
# Clona este repositorio
git clone #####################
cd #################

# Crea entorno virtual
python -m venv venv
source venv/bin/activate

# Instala dependencias
pip install -r requirements.txt
```

### 🧱 Redis con Docker

Si no tienes Redis localmente, puedes levantarlo con:

```bash
docker-compose up -d
```

### 🧪 Ejecutar la API

```bash
uvicorn main:app --reload
```

[Accede a la documentación interactiva](http://localhost:8000/docs)

## 📦 Ejemplo de uso

POST /lookup

```JSON
{
  "formula": "C6H12O6",
  "sources": ["pubchem"]
}
```

Respuesta

```JSON
{
  "source": "pubchem",
  "cached": false,
  "results": [
    {
      "cid": 5793,
      "MolecularFormula": "C6H12O6",
      "MolecularWeight": 180.16,
      "IUPACName": "(2R,3R,4R,5R)-2,3,4,5,6-pentahydroxyhexanal",
    }
  ]
}
```

### ♻️ Caché con Redis

Los resultados se guardan en Redis (de momento durante 24h) para evitar consultar de nuevo si ya hay resultados previos para la misma fórmula.

## ✨ Extensiones futuras (TODO)

- Soporte para más fuentes: ChEBI, KEGG, BioCyc, etc.
- Resolver ambigüedad de múltiples compuestos para una misma fórmula
- Cache con invalidación inteligente
- Dockerizar la API completa
