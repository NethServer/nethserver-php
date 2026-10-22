==============
nethserver-php
==============

Database example: ::

 php=configuration
    DateTimezone=Europe/Rome
    ExposePhp=
    MaxExecutionTime30=
    MemoryLimit=32
    PostMaxSize=
    ShortOpenTag=
    UploadMaxFilesize=
    MaxFileUploads=

MemoryLimit, PostMaxSize, UploadMaxFilesize are expressed in MB units.
MaxFileUploads is set by default to 20

.. warning::

   Do not set PostMaxSize above 32 MB. Keep UploadMaxFilesize below
   PostMaxSize. This limit is part of the mitigation for the PHP remote
   code execution bugs CVE-2026-109618 and CVE-2026-109619.
   See https://github.com/NethServer/dev/issues/8256
