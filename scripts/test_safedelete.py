from myapp.models import SafeParent, SafeChild1, SafeChild2, SafeChild3
import timeit
from . import timing


def run():
    starttime = timeit.default_timer()

    for i in range(10000):
        sp = SafeParent(title=f'{i}')
        sp.save()
        sc1 = SafeChild1(safeparent=sp)
        sc1.save()
        sc2 = SafeChild2(safechild1=sc1)
        sc2.save()
        sc3 = SafeChild3(safechild2=sc2)
        sc3.save()
    SafeParent.objects.all().delete()

    print("Execution time :", timeit.default_timer() - starttime)
