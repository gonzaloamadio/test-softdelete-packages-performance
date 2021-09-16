from myapp.models import SoftParent, SoftChild1, SoftChild2, SoftChild3
import timeit
from . import timing


def run():
    starttime = timeit.default_timer()

    for i in range(10000):
        sp = SoftParent(title=f'{i}')
        sp.save()
        sc1 = SoftChild1(softparent=sp)
        sc1.save()
        sc2 = SoftChild2(softchild1=sc1)
        sc2.save()
        sc3 = SoftChild3(softchild2=sc2)
        sc3.save()
    SoftParent.objects.all().delete()

    print("Execution time :", timeit.default_timer() - starttime)
