from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from ..models import Laporan,Komentar,Vote,Kecamatan,Kategori
from ..forms import LaporanForm

def index(request):
    context = {
        'title': 'Lapor ke Pemerintah',
        'semua_laporan': Laporan.objects.all()
    }
    return render(request, 'laporan/index.html', context)

def tambah(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = LaporanForm(request.POST)
            if form.is_valid():
                laporan_baru = form.save(commit=False)
                laporan_baru.pelapor = request.user
                laporan_baru.save()
                return HttpResponseRedirect('/')
        else:
            form = LaporanForm()
        return render(request, 'laporan/tambah2.html',
                      {'form': form})

    else:
        return HttpResponse('login dulu')

def laporan(request, laporan_id):
    laporan = get_object_or_404(Laporan, pk=laporan_id)
    return HttpResponse(f'''
      <h1>Detail Laporan: {laporan.judul}</h1> <br>
      {laporan.deskripsi} <br>
      oleh: {laporan.pelapor}
    ''')

def kategori(request, kategori):
    return HttpResponse(f'Kategori Laporan: {kategori}')
def kecamatan(request, kecamatan):
    return HttpResponse(f'Kecamatan Laporan: {kecamatan}')