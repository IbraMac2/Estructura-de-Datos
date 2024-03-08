class Evaluator:
    def __init__(self):
        self.stack = []

    def evaluate_postfix(self, expression):
        tokens = expression.split()

        for token in tokens:
            if token.isdigit():
                self.stack.append(int(token))
            else:
                operand2 = self.stack.pop()
                operand1 = self.stack.pop()
                result = self.apply_operator(token, operand1, operand2)
                self.stack.append(result)

        return self.stack.pop()

    def evaluate_prefix(self, expression):
        tokens = expression.split()[::-1]

        for token in tokens:
            if token.isdigit():
                self.stack.append(int(token))
            else:
                operand1 = self.stack.pop()
                operand2 = self.stack.pop()
                result = self.apply_operator(token, operand1, operand2)
                self.stack.append(result)

        return self.stack.pop()

    def apply_operator(self, operator, operand1, operand2):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
        else:
            raise ValueError(f"Operador no válido: {operator}")


def main():
    evaluator = Evaluator()

    expression = input("Ingrese la expresión aritmética (en notación posfija o prefija): ")

    if expression[0].isdigit():
        result = evaluator.evaluate_postfix(expression)
    else:
        result = evaluator.evaluate_prefix(expression)

    print(f"Resultado: {result}")


if __name__ == "__main__":
    main()
