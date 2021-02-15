import re, sys

class RegexLine:
    def __init__(self,name,regex,scoped=False):
        self.name = name
        self.regex = re.compile(regex,re.DOTALL)
        self.scoped = scoped
    
    def raiseError(self, line = None):
        s = 'ERROR: ' + self.name + ' invalido'
        s += ' on line {}'.format(line) if line is not None else ''
        print(s)

ComentarioRegex = RegexLine('Comentario', r'^💭 *(?P<Comentario>.*)$')
DeclararRegex = RegexLine('Declarar', r'^📌 (?P<DataType>[🔢⏺🔤🆗]) (?P<Variables>(.[^, ]*)( ?, ?.[^, ]*)*) ?🔒$')
EscribirRegex = RegexLine('Escribir', r'^📝 ((?P<TextoFormato>🖍(?P<Texto>.*)🖍( ?, ?(.[^, ]*))*)|(?P<Variable>.[^, ]*)|(?P<Operacion>\(? *(((.[^, ]*)|\d+) *(.[^, ]*) *((.[^, ]*)|\d+)) *\)?( (.[^, ]*) *\(? *(((.[^, ]*)|\d+) *(.[^, ]*) *((.[^, ]*)|\d+)) *\)?)*)) ?🔒$')
LeerRegex = RegexLine('Leer', r'^🔍 (?P<Variable>.[^, ]*) ?🔒$')
IgualarRegex = RegexLine('Igualar', r'^(?P<Variable_a_igualar>.[^, ]*) ?➡️ ?(🖍(?P<Texto>.*)🖍|(?P<Numero>[0-9]+\.?[0-9]*)|(?P<Variable>.[^, ]*)|(?P<Operacion>\(?(((.[^, ]*)|\d+) (.[^, ]*) ((.[^, ]*)|\d+))\)?( (.[^, ]*) \(?(((.[^, ]*)|\d+) (.[^, ]*) ((.[^, ]*)|\d+))\)?)*)) ?🔒$')
SiRegex = RegexLine('Si',r'❓ (?P<Operacion>((.[^, ]*)|\d+)|\(? *(((.[^, ]*)|\d+) *(.[^, ]*) *((.[^, ]*)|\d+)) *\)?( (.[^, ]*) *\(? *(((.[^, ]*)|\d+) *(.[^, ]*) *((.[^, ]*)|\d+)) *\)?)*) 🍇$', True)
OSiRegex = RegexLine('O Si',r'🍉 ⁉️ (?P<Operacion>((.[^, ]*)|\d+)|\(? *(((.[^, ]*)|\d+) *(.[^, ]*) *((.[^, ]*)|\d+)) *\)?( (.[^, ]*) *\(? *(((.[^, ]*)|\d+) *(.[^, ]*) *((.[^, ]*)|\d+)) *\)?)*) 🍇$', True)
sinoRegex = RegexLine('Sino',r'🍉 ❗️ 🍇$', True)
MientrasRegex = RegexLine('Mientras',r'🌀 (?P<Operacion>\(? *(((.[^, ]*)|\d+) *(.[^, ]*) *((.[^, ]*)|\d+)) *\)?( (.[^, ]*) *\(? *(((.[^, ]*)|\d+) *(.[^, ]*) *((.[^, ]*)|\d+)) *\)?)*) 🍇$', True)
ForRegex = RegexLine("De", r'(?P<VariablePrincipal>.[^, ]*) 🔁 ((?P<NumeroInicial>-?\d+)|(?P<VariableInicial>.[^, ]*)) ➡️ ((?P<NumeroFinal>-?\d+)|(?P<VariableFinal>.[^, ]*)) 👣 ((?P<NumeroPaso>-?\d+)|(?P<VariablePaso>.[^, ]*)) ?🍇', True)

regexLines = {
                20: ComentarioRegex,
                11: DeclararRegex,
                12: IgualarRegex,
                13: EscribirRegex,
                14: LeerRegex,
                15: SiRegex,
                16: OSiRegex,
                17: sinoRegex,
                18: ForRegex,
                19: MientrasRegex }