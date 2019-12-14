from django.contrib import admin
from django.utils.html import format_html
from .models import Laporan, Vote, Komentar


# Additional LINE
class KomentarInLine(admin.TabularInline):
    model = Komentar
    extra = 1
class VoteInLine(admin.TabularInline):
    model = Vote
    extra = 1;

class LaporanAdmin(admin.ModelAdmin):
    inlines = (KomentarInLine,VoteInLine)
    date_hierarchy = 'timestamp'
    list_display = (
        'timestamp',
        'judul',
        'kecamatan',
        'kategori',
        'status',
        'jumlah_komentar',
        'lihat_map'
    )
    list_display_links = ('status',)
    # list_editable = ('status',)
    search_fields = ('judul',)
    list_filter = ('judul',)

    def lihat_map(self, obj):
        return format_html(
            f'<a href="\
            https://www.google.com/maps/place/{obj.kecamatan}">\
            Lihat Map\
            </a>')

admin.site.register(Laporan, LaporanAdmin)
admin.site.register(Komentar)
admin.site.register(Vote)
