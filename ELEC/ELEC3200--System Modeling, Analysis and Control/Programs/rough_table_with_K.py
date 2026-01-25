import numpy as np
import sympy as sp

# Disclaimer: 该代码由AI生成，正确性未经严格验证，仅供参考学习使用。

def routh_table(coeffs):
    """
    计算劳斯表（支持数值系数）
    
    参数:
    coeffs: 多项式系数列表，从最高阶到常数项
          例如: s^4 + 10s^3 + 35s^2 + 50s + 24 -> [1, 10, 35, 50, 24]
    
    返回:
    table: 劳斯表
    first_col: 第一列元素
    is_stable: 是否稳定
    """
    n = len(coeffs) - 1  # 多项式阶数
    
    # 初始化劳斯表
    rows = n + 1
    cols = (n + 2) // 2  # 最大列数
    
    # 创建符号表格（用字符串表示，以便处理零）
    table = [['' for _ in range(cols)] for __ in range(rows)]
    
    # 填充前两行（s^n和s^{n-1}行）
    for i in range(rows):
        if i % 2 == 0:  # 偶数行：s^n, s^{n-2}, ...
            for j in range(cols):
                idx = 2 * j  # 偶数索引
                if idx < len(coeffs):
                    table[i][j] = str(coeffs[idx])
        else:  # 奇数行：s^{n-1}, s^{n-3}, ...
            for j in range(cols):
                idx = 2 * j + 1  # 奇数索引
                if idx < len(coeffs):
                    table[i][j] = str(coeffs[idx])
    
    # 计算后续行
    for i in range(2, rows):
        for j in range(cols - 1):  # 最后一列通常为0
            if table[i-1][0] == '' or table[i-1][0] == '0':
                # 处理第一列为零的特殊情况
                table[i][j] = 'ε' if j == 0 else '0'
                continue
            
            # 正常情况：计算行列式
            try:
                # 获取元素值
                a = float(table[i-2][0]) if table[i-2][0] != '' else 0
                b = float(table[i-2][j+1]) if j+1 < cols and table[i-2][j+1] != '' else 0
                c = float(table[i-1][0]) if table[i-1][0] != '' else 0
                d = float(table[i-1][j+1]) if j+1 < cols and table[i-1][j+1] != '' else 0
                
                # 劳斯公式：-1/c * det([a b; c d])
                value = -1.0 * (a * d - b * c) / c
                
                # 格式化为字符串（避免科学计数法）
                if abs(value) < 1e-10:
                    table[i][j] = '0'
                else:
                    table[i][j] = f"{value:.6f}".rstrip('0').rstrip('.')
            except ZeroDivisionError:
                table[i][j] = '0'
    
    # 提取第一列并检查稳定性
    first_col = []
    for i in range(rows):
        if table[i][0] != '':
            val_str = table[i][0]
            if val_str == 'ε':
                first_col.append(1e-6)  # 小正数
            else:
                try:
                    first_col.append(float(val_str))
                except:
                    first_col.append(0)
        else:
            first_col.append(0)
    
    # 检查稳定性（所有第一列元素 > 0）
    is_stable = all(x > 0 for x in first_col)
    
    return table, first_col, is_stable

def routh_table_symbolic(coeffs, symbolic_param='K'):
    """
    符号计算劳斯表（支持包含K等参数的系数）
    
    参数:
    coeffs: 多项式系数列表，可以包含符号
           例如: [1, 2, 4, 'K']
    symbolic_param: 符号参数名，默认为'K'
    
    返回:
    稳定性条件（不等式）
    """
    # 使用sympy进行符号计算
    K = sp.symbols(symbolic_param, real=True)
    
    # 将字符串'K'转换为符号K
    coeffs_sym = []
    for coeff in coeffs:
        if coeff == symbolic_param:
            coeffs_sym.append(K)
        elif isinstance(coeff, str) and coeff.isalpha():
            coeffs_sym.append(sp.symbols(coeff, real=True))
        else:
            coeffs_sym.append(coeff)
    
    n = len(coeffs_sym) - 1
    rows = n + 1
    cols = (n + 2) // 2
    
    # 创建符号表格
    table = [[None for _ in range(cols)] for __ in range(rows)]
    
    # 填充前两行
    for i in range(rows):
        if i % 2 == 0:
            for j in range(cols):
                idx = 2 * j
                if idx < len(coeffs_sym):
                    table[i][j] = coeffs_sym[idx]
        else:
            for j in range(cols):
                idx = 2 * j + 1
                if idx < len(coeffs_sym):
                    table[i][j] = coeffs_sym[idx]
    
    # 符号计算后续行
    for i in range(2, rows):
        for j in range(cols - 1):
            if table[i-1][0] == 0:
                # 处理零元素（简化处理）
                table[i][j] = sp.symbols('ε') if j == 0 else 0
                continue
            
            # 使用sympy计算
            a = table[i-2][0] if table[i-2][0] is not None else 0
            b = table[i-2][j+1] if j+1 < cols and table[i-2][j+1] is not None else 0
            c = table[i-1][0] if table[i-1][0] is not None else 0
            d = table[i-1][j+1] if j+1 < cols and table[i-1][j+1] is not None else 0
            
            # 劳斯公式
            if c != 0:
                value = -1 * (a * d - b * c) / c
                table[i][j] = sp.simplify(value)
            else:
                table[i][j] = 0
    
    # 提取第一列
    first_col = []
    for i in range(rows):
        if table[i][0] is not None:
            first_col.append(table[i][0])
        else:
            first_col.append(0)
    
    # 生成稳定性条件
    conditions = []
    for i, elem in enumerate(first_col):
        if elem != 0 and elem != sp.symbols('ε'):
            # 创建不等式：元素 > 0
            conditions.append(sp.simplify(elem > 0))
    
    return table, first_col, conditions

# =================== 示例 ===================

if __name__ == "__main__":
    print("=" * 50)
    print("示例1: s^4 + 10s^3 + 35s^2 + 50s + 24")
    print("=" * 50)
    
    coeffs1 = [1, 10, 35, 50, 24]
    table1, first_col1, stable1 = routh_table(coeffs1)
    
    print("劳斯表:")
    for i, row in enumerate(table1):
        power = len(coeffs1) - 1 - i
        print(f"s^{power}:", end="\t")
        for elem in row:
            print(f"{elem:>10}", end="")
        print()
    
    print("稳定性:", "稳定" if stable1 else "不稳定")
    
    print("\n" + "=" * 50)
    print("示例2: s^4 + 2s^3 + 4s^2 + 4s + K (符号计算)")
    print("=" * 50)
    
    coeffs2 = [1, 2, 4, 4, 'K']
    table2, first_col2, conditions2 = routh_table_symbolic(coeffs2)
    
    print("符号劳斯表:")
    for i, row in enumerate(table2):
        power = len(coeffs2) - 1 - i
        print(f"s^{power}:", end="\t")
        for elem in row:
            if elem is None:
                print(f"{'':>10}", end="")
            else:
                print(f"{sp.sstr(elem):>10}", end="")
        print()
    
    
    print("\n稳定性条件 (所有 > 0):")
    for cond in conditions2:
        print(f"  {cond}")
    