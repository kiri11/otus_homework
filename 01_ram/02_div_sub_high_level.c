// Деление через вычитание, версия на языке высокого уровня

r1 = read();
r2 = read();

if (r2 == 0) {
    return null;
}

r3 = 0;

do {
    r3 += 1;
    r1 -= r2;
} while (r1 > 0);

// Вернуться на шаг назад, если меньше нуля
if (r1 != 0) {
    r1 += r2;
    r3 -= 1;
}

write(r3);
write(r1);
