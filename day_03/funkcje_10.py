# dekoratory - funkcja opakowująca inna funkcję dodatkową funkcjonalnością

def dekor(funk):
    def wew():
        print("Dekoruj")
        return funk()

    return wew


@dekor
def hej():
    print("Hej")


hej()





