## 大学院講義　数値流体力学　レポート1 発展課題4

以下のような移流拡散方程式を実装する    

<img src="https://github.com/Chappyphage/Class-Computational-Fluid-Dynamics/blob/main/formula/iryu_kakusan.png?raw=true" width="320">    

このうち移流項を以下のように1次元風上差分スキームにより離散化する．    

<img src="https://github.com/Chappyphage/Class-Computational-Fluid-Dynamics/blob/main/formula/kazakamisabun.png?raw=true" width="150">    

また，拡散項は以下のように1次の2階微分スキームにより離散化する．    

<img src="https://github.com/Chappyphage/Class-Computational-Fluid-Dynamics/blob/main/formula/kakusan_resan.png?raw=true" width="220">    

また，非定常項の離散化を以下のように行う．  

<img src="https://github.com/Chappyphage/Class-Computational-Fluid-Dynamics/blob/main/formula/hiteijyoukou.png?raw=true" width="120">   

以上により離散化した移流拡散方程式を以下に示す．  

<img src="https://github.com/Chappyphage/Class-Computational-Fluid-Dynamics/blob/main/formula/risanka_1.png?raw=true" width="570">
 
