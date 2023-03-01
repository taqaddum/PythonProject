# %%
class Animal:
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        print('enter')
        return self.name
    def __exit__(self, exc_type, exc_value, exc_tb):
        print('exit')

# %%
dog = Animal('dog')
with dog as n:
    print(n)

# %%
def func():
    with dog as n:
        print('over')
        return print(n)

# %%
func()
