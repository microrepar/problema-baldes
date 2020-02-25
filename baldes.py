
"""Implementação da super classe Balde
"""

class Balde:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self._quantidade = 0.0

  @property
  def quantidade(self):
    return self._quantidade

  @quantidade.setter
  def quantidade(self, qtde):
    if qtde <= self.capacidade:
      self._quantidade = qtde
  
  def esvaziar(self):
    self._quantidade = 0.0

  def encher(self):
    self._quantidade = self.capacidade

  def receber_conteudo(self, outro: 'Balde'):
    espaco = self.capacidade - self.quantidade
    if espaco == 0.0:
      raise Exception(f'O balde já está com a capacidade máxima de {self._quantidade} litros')
    if outro.quantidade == espaco:
      self._quantidade += outro.quantidade
      outro.esvaziar()
    elif outro.quantidade > espaco:
      self.encher()
      outro._retirar(espaco)
    else:
      self.quantidade = outro.quantidade
      outro.esvaziar()
  
  def _retirar(self, qtde):
    if self.quantidade >= qtde:
      self._quantidade = self._quantidade - qtde
    else:
      self._quantidade = qtde - self._quantidade

  def completar(self):
    self._quantidade = self.capacidade

  def __repr__(self):
    return f'{self.__class__.__name__} capacidade={self.capacidade} quatidade={self.quantidade}'  


# Classes de especializadas que extendem a super classe Balde
# Balde com capacidade de 3 litros
class Balde3(Balde):
  def __init__(self):
    super().__init__(3.0)


# Balde com capacidade de 4 litros
class Balde4(Balde):
    def __init__(self):
      super().__init__(4.0)
  
    
if __name__ == "__main__":
    
    
    # Cria instâncias b3 com capacidade de 3 litros e b4 com capacidade de 4 litros
    b3 = Balde3()
    b4 = Balde4()

    b3

    b4

    print('Encher o balde de 4 litros:')
    b4.encher()
    print('Balde4:', str(b4.quantidade)+'L', '-', 'Balde_3:', str(b3.quantidade)+'L')

    print('Passar o conteúdo do Balde de 4 litros para o Balde de 3 litros:')
    b3.receber_conteudo(b4)
    print('Balde4:', str(b4.quantidade)+'L', '-', 'Balde_3:', str(b3.quantidade)+'L')

    print('Esvaziar o Balde de 3 litros:')
    b3.esvaziar()
    print('Balde4:', str(b4.quantidade)+'L', '-', 'Balde_3:', str(b3.quantidade)+'L')

    print('Passar conteúdo restante do Balde de 4 litros para o Balde de 3 litros:')
    b3.receber_conteudo(b4)
    print('Balde4:', str(b4.quantidade)+'L', '-', 'Balde_3:', str(b3.quantidade)+'L')

    print('Encher o balde de 4 litros:')
    b4.encher()
    print('Balde4:', str(b4.quantidade)+'L', '-', 'Balde_3:', str(b3.quantidade)+'L')

    print('Passar o conteúdo do Balde de 4 litros para o Balde de 3 litros:')
    b3.receber_conteudo(b4)
    print('Balde4:', str(b4.quantidade)+'L', '-', 'Balde_3:', str(b3.quantidade)+'L')

    
    