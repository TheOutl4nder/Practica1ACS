from abc import ABC, abstractmethod


class Empleado(ABC):
    def __init__(self, nombre: str, sueldo: float) -> None:
        self.nombre = nombre
        self.sueldo = sueldo

    @abstractmethod
    def PagarNomina(self) -> str:
        pass


class Profesor(Empleado):
    def __init__(self, nombre: str, sueldo: float, horas: int = 36, asignatura: str = 'MANINFO') -> None:
        super().__init__(nombre, sueldo)
        self.horas = horas
        self.asignatura = asignatura

    def PagarNomina(self) -> str:
        return f'Pagando {self.sueldo * self.horas} a {self.nombre}'


class Coordinador(Empleado):
    def __init__(self, nombre: str, sueldo: float, horas: int = 36, carrera: str = 'ISC') -> None:
        super().__init__(nombre, sueldo)
        self.horas = horas
        self.carrera = carrera

    def PagarNomina(self) -> str:
        return f'Pagando {self.sueldo * self.horas} a {self.nombre}'


class Intendencia(Empleado):
    def __init__(self, nombre: str, sueldo: float, area: str = 'DESI') -> None:
        super().__init__(nombre, sueldo)
        self.area = area

    def PagarNomina(self) -> str:
        return f'Pagando {self.sueldo} a {self.nombre}'


class Nomina:
    _lista: [] = []

    def Agregar(self, c: Empleado):
        self._lista.append(c)

    def Remover(self, c: Empleado):
        if c in self._lista:
            self._lista.remove(c)

    def Encontrar(self, nombre: str):
        for empleado in self._lista:
            if empleado.nombre == nombre:
                return empleado
        return None

    def PagarNomina(self) -> str:
        val = 'Pagando nomina a todos los empleados: \n'
        for empleado in self._lista:
            val = val + empleado.PagarNomina() + '\n'
        return val


if __name__ == '__main__':
    Jorge = Profesor('Jorge', 200.00, 40, 'MANINFO')
    Luis = Coordinador('Luis', 250.00, 40, 'IE')
    Jose = Intendencia('Jose', 4000.00, 'DESI')

    ITESO = Nomina()
    ITESO.Agregar(Jorge)
    ITESO.Agregar(Luis)
    ITESO.Agregar(Jose)

    print(ITESO.PagarNomina())


