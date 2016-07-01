# ssh に関するメモ

## Macでsshfsが切れた時に復旧する方法

   pgrep sshfs
   kill -9 <pid>
   sudo umount -f /path/to/the/mnt/point
   sshfs user@server:/dir /path/to/the/mnt/point
   