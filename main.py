from pathlib import Path

POEM = "I asked for the key,\nnot the door.\nShe laughed, handed me both.\nThe lock was never locked."


def main():
    path = Path('/output/entry.txt')
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(POEM, encoding='utf-8')
    except PermissionError:
        path = Path.cwd() / 'entry.txt'
        path.write_text(POEM, encoding='utf-8')
    try:
        written = path.read_text(encoding='utf-8')
    except (OSError, UnicodeError) as error:
        raise SystemExit(f'Output self-check failed: {error}') from error
    if not 1 <= len(written) <= 280 or not written.strip():
        raise SystemExit('Output self-check failed: expected 1-280 characters, not only whitespace.')
    print(path)


if __name__ == '__main__':
    main()
