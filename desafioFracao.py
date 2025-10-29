class Fracao:
    def __init__(self, num, den):
        if den == 0:
            raise ValueError("Denominador não pode ser zero.")
        if den < 0:
            num = -num
            den = -den
        self.__num = int(num)
        self.__den = int(den)
        self.simplifica()

    def __str__(self):
        inteiro = self.__num // self.__den
        resto = abs(self.__num % self.__den)
        if resto == 0:
            return str(inteiro)
        elif abs(inteiro) == 0:
            return f"{resto}/{self.__den}"
        else:
            # agora sem espaço entre inteiro e fração
            return f"{inteiro}{resto}/{self.__den}"

    @property
    def num(self):
        return self.__num

    @property
    def den(self):
        return self.__den

    def mdc(self, m, n):
        m = abs(int(m))
        n = abs(int(n))
        while n:
            m, n = n, m % n
        return m

    def simplifica(self):
        divComum = self.mdc(self.__num, self.__den)
        if divComum != 0:
            self.__num //= divComum
            self.__den //= divComum
        if self.__den < 0:
            self.__num = -self.__num
            self.__den = -self.__den

    def __add__(self, outraFrac):
        novoNum = self.__num * outraFrac.den + self.__den * outraFrac.num
        novoDen = self.__den * outraFrac.den
        return Fracao(novoNum, novoDen)

    def fracaoMista(self, num1, den1, num2, den2):
        frac1 = Fracao(num1, den1)
        frac2 = Fracao(num2, den2)
        soma = frac1 + frac2
        print(soma)


if __name__ == '__main__':
    f = Fracao(1, 1)
    f.fracaoMista(7, 6, 13, 7)   # 3 1/42 → agora "31/42"
    f.fracaoMista(1, 3, 2, 3)    # 1
    f.fracaoMista(7, 2, 14, 3)   # 8 1/6 → agora "81/6"