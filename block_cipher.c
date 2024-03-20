#include <stdint.h>
#include <string.h>
#include <stdio.h>

void encrypt (uint32_t v[2], const uint32_t k[4]) {
    uint32_t v0=v[0], v1=v[1], sum=0, i;
    uint32_t delta=0x9E3779B9;
    uint32_t k0=k[0], k1=k[1], k2=k[2], k3=k[3];
    for (i=0; i<32; i++) {
        sum += delta;
        v0 += ((v1<<4) + k0) ^ (v1 + sum) ^ ((v1>>5) + k1);
        v1 += ((v0<<4) + k2) ^ (v0 + sum) ^ ((v0>>5) + k3);
    }
    v[0]=v0; v[1]=v1;
}

void decrypt (uint32_t v[2], const uint32_t k[4]) {
    uint32_t v0=v[0], v1=v[1], sum=0xC6EF3720, i;
    uint32_t delta=0x9E3779B9;
    uint32_t k0=k[0], k1=k[1], k2=k[2], k3=k[3];
    for (i=0; i<32; i++) {
        v1 -= ((v0<<4) + k2) ^ (v0 + sum) ^ ((v0>>5) + k3);
        v0 -= ((v1<<4) + k0) ^ (v1 + sum) ^ ((v1>>5) + k1);
        sum -= delta;
    }
    v[0]=v0; v[1]=v1;
}

void char_to_block(uint32_t* v, const char* message) {
    v[0] = 0; v[1] = 0;
    for (int j = 0; j < 4 && *(message+j); ++j)
        v[0] += message[j] << (j * 8);
    for (int j = 4; j < 8 && *(message+j); ++j)
        v[1] += message[j] << ((j - 4) * 8);
}

void block_to_char(uint32_t* v, char* message) {
    for (int i = 0; i < 4; ++i) {
        message[i] = (v[0] >> (i * 8)) & 0xff;
    }
    for (int i = 0; i < 4; ++i) {
        message[i + 4] = (v[1] >> (i * 8)) & 0xff;
    }
}

int main() {
    int n = 20;
    char* message = "Hi, it's me, Rovers!";
    uint32_t sandbox[6];
    int nblocks = (n + 8 - 1) / 8;
    printf("nblocks: %d\n", nblocks);

    char decrypted[20];
    uint32_t k[4] = {1, 2, 3, 4};
    printf("plain: %s\n", message);
    for (int i = 0; i < nblocks; ++i) {
        char_to_block(sandbox + i * 2, message + i * 8);
    }
    printf("plain   bytes: ");
    for (int i = 0; i < nblocks; ++i)
        printf("%x %x ", sandbox[2*i], sandbox[2*i+1]);
    // encrypt!
    for (int i = 0; i < nblocks; ++i)
        encrypt(sandbox + 2 * i, k);
    printf("\n");
    printf("encrypt bytes: ");
    for (int i = 0; i < nblocks; ++i)
        printf("%x %x ", sandbox[2*i], sandbox[2*i+1]);
    printf("\n");

    // decrypt!
    for (int i = 0; i < nblocks; ++i)
        decrypt(sandbox + 2 * i, k);

    printf("decrypt bytes: ");
    for (int i = 0; i < nblocks; ++i)
        printf("%x %x ", sandbox[2*i], sandbox[2*i+1]);
    printf("\n");

    for (int i = 0; i < nblocks; ++i) {
        block_to_char(sandbox + i * 2, decrypted + i * 8);
    }
    printf("decrypted: %s\n", decrypted);
}
