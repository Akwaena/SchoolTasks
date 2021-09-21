def trans_from_infix(A, form):
    A = A.split()
    error = False
    while ('(' in A) or (')' in A):
        numS = 0
        numE = 0
        if len(A) == 2:
            error = True
            break
        for num in range(len(A)):
            if A[num] == '(':
                numS = num
        for num in range(len(A)):
            if A[num + numS] == ')':
                numE = num + numS
                break
        part = A[numS + 1:numE]
        while ('*' in part) or ('^' in part) or ('/' in part):
            if len(A) == 2:
                error = True
                break
            for num in range(len(part)):
                if (part[num] == '*') or (part[num] == '/') or (part[num] == '^'):
                    if form == 'postfix': part[num + 1] = str(part[num - 1]) + ' ' + str(part[num + 1]) + ' ' + str(
                        part[num])
                    if form == 'prefix':  part[num + 1] = str(part[num]) + ' ' + str(part[num - 1]) + ' ' + str(
                        part[num + 1])
                    del part[num - 1:num + 1]
                    break
        while ('-' in part) or ('+' in part):
            if len(A) == 2:
                error = True
                break
            for num in range(len(part)):
                if (part[num] == '-') or (part[num] == '+'):
                    if form == 'postfix': part[num + 1] = str(part[num - 1]) + ' ' + str(part[num + 1]) + ' ' + str(
                        part[num])
                    if form == 'prefix':  part[num + 1] = str(part[num]) + ' ' + str(part[num - 1]) + ' ' + str(
                        part[num + 1])
                    del part[num - 1:num + 1]
                    break
        A[numE] = part[0]
        del A[numS:numE]
    while ('*' in A) or ('^' in A) or ('/' in A):
        if len(A) == 2:
            error = True
            break
        for num in range(len(A)):
            if (A[num] == '*') or (A[num] == '/') or (A[num] == '^'):
                if form == 'postfix': A[num + 1] = str(A[num - 1]) + ' ' + str(A[num + 1]) + ' ' + str(A[num])
                if form == 'prefix':  A[num + 1] = str(A[num]) + ' ' + str(A[num - 1]) + ' ' + str(A[num + 1])
                del A[num - 1:num + 1]
                break
    while ('-' in A) or ('+' in A):
        if len(A) == 2:
            error = True
            break
        for num in range(len(A)):
            if (A[num] == '-') or (A[num] == '+'):
                if form == 'postfix': A[num + 1] = str(A[num - 1]) + ' ' + str(A[num + 1]) + ' ' + str(A[num])
                if form == 'prefix':  A[num + 1] = str(A[num]) + ' ' + str(A[num - 1]) + ' ' + str(A[num + 1])
                del A[num - 1:num + 1]
                break
    return [str(A[0]), error]
