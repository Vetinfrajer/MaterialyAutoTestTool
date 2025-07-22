# Material Auto Test Tool

Moderní univerzální desktopová aplikace pro testování chatbot materiálů a scénářů.

## Požadavky
- Python 3.8+
- Knihovny: PyQt5, requests, pyyaml

Nainstaluj je příkazem:
```bash
pip3 install PyQt5 requests pyyaml
```

## Spuštění aplikace
1. Zkopíruj všechny soubory do libovolné složky.
2. Spusť aplikaci:
   ```bash
   python3 MaterialAutoTestToolApp_qt.py
   ```

## Použití
1. **Zadej endpoint chatbota** (např. `http://127.0.0.1:1234`) a ulož.
2. **Vlož obsah materiálu** (context1.txt) a YAML scénáře do příslušných polí (nebo použij tlačítko „Vložit ze schránky“).
3. Klikni na **Spustit test**.
4. Výsledky a souhrn se zobrazí v aplikaci.

- Všechny potřebné soubory (`context1.txt`, `test_core_messenger_and_inbox.yaml`, `endpoint.txt`) se ukládají automaticky do aktuální složky.
- Aplikace je přenositelná a nevyžaduje žádné úpravy kódu.

## Poznámky
- Pokud používáš Windows, změň příkaz `python3` na `python` podle své instalace.
- Pro balení do .app nebo .exe lze použít PyInstaller nebo Platypus (návod na vyžádání).

---

**Autor:**
Tým Material Auto Test Tool 