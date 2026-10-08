"""Environment check: `python -m src.check` should print 'todo listo'."""
import importlib
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
LIBS = ["pandas", "duckdb", "pyarrow", "geopandas", "shapely", "requests", "sklearn", "statsmodels", "streamlit", "pydeck", "folium", "plotly"]
FOLDERS = ["data/raw", "data/processed", "sql", "src", "notebooks", "app", "docs"]


def main() -> int:
    ok = True
    print(f"Python {sys.version.split()[0]}")
    for lib in LIBS:
        try:
            m = importlib.import_module(lib)
            print(f"  ok  {lib} {getattr(m, '__version__', '')}")
        except ImportError as e:
            ok = False
            print(f"  FALTA {lib}: {e}")
    for f in FOLDERS:
        p = ROOT / f
        p.mkdir(parents=True, exist_ok=True)
    import duckdb
    con = duckdb.connect(str(ROOT / "data" / "lotlens.duckdb"))
    con.execute("select 1").fetchone()
    con.close()
    print("  ok  base DuckDB en data/lotlens.duckdb")
    print("todo listo" if ok else "faltan librerías")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
