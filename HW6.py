def reverse(st):
    line_split = st.split()
    line_revers = line_split[::-1]
    return ' '.join(line_revers)