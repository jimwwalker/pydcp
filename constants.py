

# Header formatting an codes
PKT_HEADER_FMT =">BBHBBHIIQ"

HEADER_LEN = 24

REQ_MAGIC = 0x80
RES_MAGIC = 0x81

# UPR command opcodes
CMD_OPEN             = 0x50
CMD_ADD_STREAM       = 0x51
CMD_CLOSE_STREAM     = 0x52
CMD_STREAM_REQ       = 0x53
CMD_GET_FAILOVER_LOG = 0x54
CMD_STREAM_END       = 0x55
CMD_SNAPSHOT_MARKER  = 0x56
CMD_MUTATION         = 0x57
CMD_DELETION         = 0x58
CMD_EXPIRATION       = 0x59
CMD_FLUSH            = 0x5a
CMD_SET_VB_STATE     = 0x5b

# Memcached command opcodes

CMD_SET    = 0x01
CMD_DELETE = 0x04
CMD_FLUSH  = 0x08
CMD_STATS  = 0x10

# Flag values
FLAG_OPEN_CONSUMER = 0x00
FLAG_OPEN_PRODUCER = 0x01

# Error Codes
SUCCESS             = 0x00
ERR_KEY_ENOENT      = 0x01
ERR_KEY_EEXISTS     = 0x02
ERR_E2BIG           = 0x03
ERR_EINVAL          = 0x04
ERR_NOT_STORED      = 0x05
ERR_DELTA_BADVAL    = 0x06
ERR_NOT_MY_VBUCKET  = 0x07
ERR_AUTH_ERROR      = 0x20
ERR_AUTH_CONTINUE   = 0x21
ERR_ERANGE          = 0x22
ERR_ROLLBACK        = 0x23
ERR_UNKNOWN_COMMAND = 0x81
ERR_ENOMEM          = 0x82
ERR_NOT_SUPPORTED   = 0x83
ERR_EINTERNAL       = 0x84
ERR_EBUSY           = 0x85
ERR_ETMPFAIL        = 0x86
ERR_ECLIENT         = 0xff
