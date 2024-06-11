from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, PositiveIntegerField, ForeignKey, CASCADE, EmailField, DateTimeField
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field
from parler.models import TranslatableModel, TranslatedFields


class User(AbstractUser):
    first_name = CharField(verbose_name=_('first_name'), max_length=50)
    last_name = CharField(verbose_name=_('last_name'), max_length=50)
    username = CharField(verbose_name=_('username'), max_length=50, unique=True)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=CharField(verbose_name=_('category_name'), max_length=75)
    )

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(TranslatableModel):
    translations = TranslatedFields(
        title=CharField(verbose_name=_('product_title'), max_length=75),
        description=CKEditor5Field(verbose_name=_('product_description'), config_name='extends')
    )
    price = PositiveIntegerField(verbose_name=_('product_price'))
    quantity = PositiveIntegerField(verbose_name=_('product_quantity'))
    category = ForeignKey(verbose_name=_('product_category'), to='apps.Category', on_delete=CASCADE)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class NewsReceiver(Model):
    email = EmailField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('News_Receiver')
        verbose_name_plural = _('News_Receivers')
