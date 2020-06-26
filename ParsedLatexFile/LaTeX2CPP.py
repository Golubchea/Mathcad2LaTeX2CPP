

from sys import path as syspath
from os import path as ospath
import sys
import os
import string
#import multidict
import re
dirpath = os.getcwd()
print(dirpath)
sys.path.append(dirpath+"/libs/sympy")
#syspath.append("/home/e/code_camera/Mathcad2LaTeX/data/ParsedLatexFile/libs/sympy/sympy")
from sympy.parsing.latex import parse_latex
from sympy import Symbol
import sympy
sympy.init_printing()

filepath = sys.argv[1]

filepath = filepath[:-4]
orig_stdout = sys.stdout
f = open(filepath+".h", 'w')
sys.stdout = f


count=0



with open(sys.argv[1]) as fp:
   line = fp.readline()
   latexAformula = False
   while line:
       #print("START+"+line.strip()+"+END")
       if(line.strip()=="\\begin{align}"):
          #print("----------start---------")
          line = fp.readline()
          #line="%r"%line
          v_1=line

          line=line.replace("sin",r"\sin")
          line=line.replace("cos",r"\cos")
          line=line.replace("tan",r"\tan")
          line=line.replace("cot",r"\cot")

          line=line.replace(r"\left",' ')
          line=line.replace(r"\right",' ')
          line=line.replace('\n',' ')


          #get all variables
          v_1=v_1.replace(r"\left",' ')
          v_1=v_1.replace(r"\right",' ')
          v_1=v_1.replace("sin","")
          v_1=v_1.replace("cos","")

          v_1=v_1.replace("sin","")
          v_1=v_1.replace("cos","")
          v_1=v_1.replace(r"=","")
          v_1=v_1.replace(r"\frac","")
          v_1=v_1.replace(r"\cdot","")
          v_1=v_1.replace("\cdot","")
          v_1=v_1.replace("cdot","")
          v_1=v_1.replace("(","")
          v_1=v_1.replace("+","")
          v_1=v_1.replace("-","")
          v_1=v_1.replace(")","")
          v_1=v_1.replace("{","")
          v_1=v_1.replace("}","")
          vars_set=" ".join(v_1.split())
          
          vars_set = set(vars_set.strip().split(' ') )
          #sorted(vars_list,reverse=True)
          
          
          
          vars_list=list(vars_set)
          vars_list=sorted(vars_list, key=len,reverse=True) 
          
          


          VARS=string.ascii_uppercase[:len(vars_list)]
          
          counter=0


          for i in vars_list:
             
             line=line.replace(i,VARS[counter])

             #line=line.replace(i,"\mathit{"+VARS[counter]+"}")
             counter=counter+1

          #counter = 0

          expr = parse_latex(line)

          OUT_var = str(expr.lhs)
          indx=VARS.index(OUT_var)

          #VARS.replace(VARS[indx],"")

          answer = "double " + filepath + "_" + vars_list[indx] + "( \n"
          vars_list[indx] = ""
          for i in range(len(vars_list)):
             #print(i)
             if(vars_list[i]==""):
                s=''
             elif(i==len(vars_list)-1):
                answer = answer + "double " + vars_list[i] + ") \n"
             else:
                answer =answer +"double " + vars_list[i]+", \n"

          answer = answer+"{ \n"

          answer = answer + "return "  + str(expr.rhs) + "; \n"
          answer = answer +"} \n"
          for i in range(len(vars_list)):
             answer=answer.replace(VARS[i] ,vars_list[i])



           #     print("" + VARS[i] + " = " + vars_list[i] + ";")


          print(answer)
          #sympy.pprint(expr)
          #print("---------------end--------------")  
          count=count+1
       else:
          line = fp.readline()
 

sys.stdout = orig_stdout
f.close()
#expr = parse_latex(test)  

#print(expr)  
#print(expr.evalf(4, subs=dict(l=5, t=3.141))  )  
