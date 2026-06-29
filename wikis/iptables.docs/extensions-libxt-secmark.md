# Extensions / Libxt SECMARK

This is used to set the security mark value associated with the packet for use by security subsystems such as SELinux. It is valid in the **security** table (for backwards compatibility with older kernels, it is also valid in the **mangle** table). The mark is 32 bits wide.

**--selctx** *security_context*
