# Author: Christiano Braga
# http://github.com/ChristianoBraga

import pi

class Impiler(object):
    def identifier(self, ast):
        return pi.Id(str(ast))

    def number(self, ast):
        return pi.Num(int(ast))

    def addition(self, ast):
        return pi.Sum(ast.left, ast.right)

    def subtraction(self, ast):
        return pi.Sub(ast.left, ast.right)

    def multiplication(self, ast):
        return pi.Mul(ast.left, ast.right)

    def division(self, ast):
        return pi.Div(ast.left, ast.right)

    def truth(self, ast):
        return pi.Boo(bool(ast))

    def negation(self, ast):
        return pi.Not(ast.b)    

    def equality(self, ast):
        return pi.Eq(ast.left, ast.right)

    def lowerthan(self,ast):
        return pi.Lt(ast.left, ast.right)

    def greaterthan(self,ast):
        return pi.Gt(ast.left, ast.right)

    def lowereq(self,ast):
        return pi.Le(ast.left, ast.right)

    def greatereq(self,ast):
        return pi.Ge(ast.left, ast.right)

    def conjunction(self, ast):
        return pi.And(ast.left, ast.right)

    def disjunction(self, ast):
        return pi.Or(ast.left, ast.right)

    def nop(self, ast):
        return pi.Nop()

    def assign(self, ast):
        return pi.Assign(ast.id, ast.e)

    def cnst(self, ast):
        return pi.Bind(ast.id, ast.e)

    def var(self, ast):
        return pi.Bind(ast.id, pi.Ref(ast.e))

    def let(self, ast):
        if isinstance(ast.c, pi.Cmd):
            return pi.Blk(ast.d, ast.c)
        elif isinstance(ast.c, list):
            cmd = ast.c[0]
            for i in range(1, len(ast.c)):
                cmd = pi.CSeq(cmd, ast.c[i])
            return pi.Blk(ast.d, cmd)

    def loop(self, ast):
        if isinstance(ast.c, pi.Cmd):
            return pi.Loop(ast.e, ast.c)
        else:
            cmd = ast.c[0]
            for i in range(1, len(ast.c)):
                cmd = pi.CSeq(cmd, ast.c[i])
            return pi.Loop(ast.e, cmd)

        
    def cond(self, ast):
        cmd1 = ast.c1
        cmd2 = ast.c2

        if not(isinstance(cmd1, pi.Cmd)):
            for i in range(1, len(ast.c1)):
                cmd1 = pi.CSeq(cmd1, ast.c1[i])

        if not(isinstance(cmd2, pi.Cmd)):
            for i in range(1, len(ast.c2)):
                cmd2 = pi.CSeq(cmd2, ast.c2[i])

        return pi.Cond(ast.e, cmd1, cmd2)
        
        
    def __makeAbs(self, f, c):
        if isinstance(c, pi.Blk):
            body = c
        else:
            body = pi.Blk(c)

        if f == []:
            return pi.Abs(pi.Formals(), body)
        else:
            formals = []
            for k,v in f.items():
                if not v == None:
                    formals.append(v)
            return pi.Abs(formals, body)

    def fn(self, ast):
        abs = self.__makeAbs(ast.f, ast.c)
        return pi.BindAbs(ast.id, abs)

    def call(self, ast):
        actuals = []
        for k,v in ast.a.items():
            if not v == None:
                actuals.append(v)
        return pi.Call(ast.i, actuals)
