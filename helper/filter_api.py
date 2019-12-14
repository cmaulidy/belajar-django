from rest_framework.permissions import BasePermission

	
class BlacklistPermission(BasePermission):
#   Global permission check for blacklisted IPs.
  def has_permission(self, request, view):
      ip_addr = request.META['REMOTE_ADDR']
      List_IP = ('172.17.7.221','127.0.0.1')

    #   blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
      blacklisted = ip_addr in List_IP
      return blacklisted

      # return True --> bisa akses
      # return false --> tidak bisa akses
