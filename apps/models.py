from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, PositiveIntegerField, ForeignKey, CASCADE, EmailField, DateTimeField, \
    ImageField
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field
from parler.models import TranslatableModel, TranslatedFields

from apps.tasks import task_send_email


class BaseDateTimeModel(Model):
    created_at = DateTimeField(verbose_name=_('created_at'), auto_now_add=True)
    updated_at = DateTimeField(verbose_name=_('updated_at'), auto_now=True)

    class Meta:
        abstract = True


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

    def __str__(self):
        return self.name

    def count_product(self):
        return self.product_set.count()


class Country(TranslatableModel):
    translations = TranslatedFields(
        name=CharField(verbose_name=_('country_name'), max_length=75)
    )

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

    def __str__(self):
        return self.name


class Product(TranslatableModel, BaseDateTimeModel):
    translations = TranslatedFields(
        title=CharField(verbose_name=_('product_title'), max_length=75),
        description=CKEditor5Field(verbose_name=_('product_description'), config_name='extends')
    )
    image = ImageField(verbose_name=_('product_image'), upload_to='category/images')
    price = PositiveIntegerField(verbose_name=_('product_price'))
    quantity = PositiveIntegerField(verbose_name=_('product_quantity'))
    category = ForeignKey(verbose_name=_('product_category'), to='apps.Category', on_delete=CASCADE)
    country = ForeignKey(verbose_name=_('product_country'), to='apps.Country', on_delete=CASCADE)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title

    def count_product(self):
        return self.product_set.count()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        is_new_instance = self.pk is None
        super().save(force_insert, force_update, using, update_fields)

        if is_new_instance:
            all_emails = list(NewsReceiver.objects.values_list('email', flat=True))
            task_send_email.delay('LUCH STOM INTERPRISE', self.title, all_emails)


class NewsReceiver(BaseDateTimeModel):
    email = EmailField(unique=True)

    class Meta:
        verbose_name = _('News_Receiver')
        verbose_name_plural = _('News_Receivers')


class New(TranslatableModel, BaseDateTimeModel):
    translations = TranslatedFields(
        title=CharField(verbose_name=_('new_title'), max_length=255),
        description=CKEditor5Field(verbose_name=_('new_description'), config_name='extends')
    )
    image = ImageField(upload_to='news/images', verbose_name=_('new_image'))

    class Meta:
        verbose_name = _('New')
        verbose_name_plural = _('News')
