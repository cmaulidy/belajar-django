from rest_framework import viewsets, permissions
from django.http import JsonResponse
from ..models import Laporan,Komentar,Vote,Kecamatan,Kategori
from ..serializers import LaporanSerializers,KomentarSerializers,VoteSerializers,KecamatanSerializers,KategoriSerializers
from helper import BlacklistPermission

def rest(request):
    data = {
        'id' : 1,
        'name' : 'Syaiful',
        'laporan' : Laporan.objects.all()
    }
    return JsonResponse(data)
class LaporanRestView(viewsets.ModelViewSet):
    queryset = Laporan.objects.all()
    serializer_class = LaporanSerializers
    permission_classes = (permissions.IsAuthenticated,BlacklistPermission)
class KomentarRestView(viewsets.ModelViewSet):
    queryset = Komentar.objects.all()
    serializer_class = KomentarSerializers
class VoteRestView(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializers
class KecamatanRestView(viewsets.ModelViewSet):
    queryset = Kecamatan.objects.all()
    serializer_class = KecamatanSerializers
class KategoriRestView(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializers