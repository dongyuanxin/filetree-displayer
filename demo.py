try:
    from .displayer import Filetree
except:
    from displayer import Filetree


if __name__=='__main__':
    shower = Filetree()
    shower.set_root('test')
    shower.show()

    shower.set_root('test2')
    shower.show()