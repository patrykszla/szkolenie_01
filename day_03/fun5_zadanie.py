

def kantor(curr):
    def usd(kwota):
        return 4.1 * kwota
    def eur(kwota):
        return 3.86 * kwota

    if curr == 'usd':
        return usd
    elif curr == 'eur':
        return eur



test = kantor('eur')
print(test(5))