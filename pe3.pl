# project euler 3 using perel

# What is the largest prime factor of the number 600851475143 ?

#!/usr/bin/perl
use strict;
use warnings;

my $x = 600851475143; # input
my @a;
my @p;
my @m;

# factor the prime numbers of an integer

for (my $i = 2; $i <= $x; $i++) {
    for (my $z = 2; $z <= $i; $z++) {
         push @p, $z unless $i % $z;
    }
    push @a, pop @p if $#p == 0;
    @p = ();
}

# put prime numbers into an array
push @m, $_, "\n" foreach @a;

#get last number in array using $#
print $#m




