# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class DeletionRecoveryLevel(str, Enum):

    purgeable = "Purgeable"
    recoverable_purgeable = "Recoverable+Purgeable"
    recoverable = "Recoverable"
    recoverable_protected_subscription = "Recoverable+ProtectedSubscription"
    customized_recoverable_purgeable = "CustomizedRecoverable+Purgeable"
    customized_recoverable = "CustomizedRecoverable"
    customized_recoverable_protected_subscription = "CustomizedRecoverable+ProtectedSubscription"


class JsonWebKeyType(str, Enum):

    ec = "EC"
    ec_hsm = "EC-HSM"
    rsa = "RSA"
    rsa_hsm = "RSA-HSM"
    oct = "oct"
    oct_hsm = "oct-HSM"


class JsonWebKeyCurveName(str, Enum):

    p_256 = "P-256"
    p_384 = "P-384"
    p_521 = "P-521"
    p_256_k = "P-256K"


class KeyUsageType(str, Enum):

    digital_signature = "digitalSignature"
    non_repudiation = "nonRepudiation"
    key_encipherment = "keyEncipherment"
    data_encipherment = "dataEncipherment"
    key_agreement = "keyAgreement"
    key_cert_sign = "keyCertSign"
    c_rl_sign = "cRLSign"
    encipher_only = "encipherOnly"
    decipher_only = "decipherOnly"


class ActionType(str, Enum):

    email_contacts = "EmailContacts"
    auto_renew = "AutoRenew"


class JsonWebKeyOperation(str, Enum):

    encrypt = "encrypt"
    decrypt = "decrypt"
    sign = "sign"
    verify = "verify"
    wrap_key = "wrapKey"
    unwrap_key = "unwrapKey"
    import_enum = "import"


class JsonWebKeyEncryptionAlgorithm(str, Enum):

    rsa_oaep = "RSA-OAEP"
    rsa_oaep_256 = "RSA-OAEP-256"
    rsa1_5 = "RSA1_5"
    a128_gcm = "A128GCM"
    a192_gcm = "A192GCM"
    a256_gcm = "A256GCM"
    a128_kw = "A128KW"
    a192_kw = "A192KW"
    a256_kw = "A256KW"


class JsonWebKeySignatureAlgorithm(str, Enum):

    ps256 = "PS256"  #: RSASSA-PSS using SHA-256 and MGF1 with SHA-256, as described in https://tools.ietf.org/html/rfc7518
    ps384 = "PS384"  #: RSASSA-PSS using SHA-384 and MGF1 with SHA-384, as described in https://tools.ietf.org/html/rfc7518
    ps512 = "PS512"  #: RSASSA-PSS using SHA-512 and MGF1 with SHA-512, as described in https://tools.ietf.org/html/rfc7518
    rs256 = "RS256"  #: RSASSA-PKCS1-v1_5 using SHA-256, as described in https://tools.ietf.org/html/rfc7518
    rs384 = "RS384"  #: RSASSA-PKCS1-v1_5 using SHA-384, as described in https://tools.ietf.org/html/rfc7518
    rs512 = "RS512"  #: RSASSA-PKCS1-v1_5 using SHA-512, as described in https://tools.ietf.org/html/rfc7518
    rsnull = "RSNULL"  #: Reserved
    es256 = "ES256"  #: ECDSA using P-256 and SHA-256, as described in https://tools.ietf.org/html/rfc7518.
    es384 = "ES384"  #: ECDSA using P-384 and SHA-384, as described in https://tools.ietf.org/html/rfc7518
    es512 = "ES512"  #: ECDSA using P-521 and SHA-512, as described in https://tools.ietf.org/html/rfc7518
    es256_k = "ES256K"  #: ECDSA using P-256K and SHA-256, as described in https://tools.ietf.org/html/rfc7518


class SasTokenType(str, Enum):

    account = "account"
    service = "service"
