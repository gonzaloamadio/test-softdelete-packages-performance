from django.db import models
from softdelete.models import SoftDeleteObject
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE

# SAFE DELETE MODELS


class SafeParent(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    title = models.CharField(max_length=10)


class SafeChild1(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    safeparent = models.ForeignKey(SafeParent, on_delete=models.CASCADE)


class SafeChild2(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    safechild1 = models.ForeignKey(SafeChild1, on_delete=models.CASCADE)


class SafeChild3(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    safechild2 = models.ForeignKey(SafeChild2, on_delete=models.CASCADE)


# SOFT DELETE MODELS

class SoftParent(SoftDeleteObject, models.Model):
    title = models.CharField(max_length=10)


class SoftChild1(SoftDeleteObject, models.Model):
    softparent = models.ForeignKey(SoftParent, on_delete=models.CASCADE)


class SoftChild2(SoftDeleteObject, models.Model):
    softchild1 = models.ForeignKey(SoftChild1, on_delete=models.CASCADE)


class SoftChild3(SoftDeleteObject, models.Model):
    softchild2 = models.ForeignKey(SoftChild2, on_delete=models.CASCADE)
