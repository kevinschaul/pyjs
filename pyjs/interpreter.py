class Interpreter(object):

    def interpret(tree):
        pass

    def eval_expr(tree, env):
        exptype = tree[0]

        if exptype == 'function':
            fparams = tree[1]
            fbody = tree[2]
            return ('function', fparams, fbody, env)
