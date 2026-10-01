r1 = float(input("Digite o tamanho da reta 1: "))
r2 = float(input("Digite o tamanho da reta 2: "))
r3 = float(input("Digite o tamanho da reta 3: "))

if r1+r2>r3 and r2+r3>r1 and r3+r2>r1:
    print ('As retas podem formar um triângulo')
else:
    print('As retas não podem formar um triângulo')

# CORES NO TERMINAL
# \033[style;text;backm
# style: 0 - none; 1 - bold; 4 - underline; 7 - negative;

# text: 30 - white; 31 - red; 32 - green; 33 - yellow; 
# 34 - blue; 35 - purple; 36 - ciano; 37 - gray;

# back: 40 - white; 41 - red; 42 - green; 43 - yellow; 
# 44 - blue; 45 - purple; 46 - ciano; 47 - gray;