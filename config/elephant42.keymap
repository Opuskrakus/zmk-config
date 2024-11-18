/*
 * Copyright (c) 2021 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 */
 
#include <behaviors.dtsi>
#include <dt-bindings/zmk/keys.h>
#include <dt-bindings/zmk/bt.h>
#include <dt-bindings/zmk/outputs.h>

// #include <dt-bindings/zmk/rgb.h>
// #include <dt-bindings/zmk/backlight.h>
#include <dt-bindings/zmk/ext_power.h>
// #include <dt-bindings/zmk/mouse.h>

#include "keys_sv.h"

#define BASE 0
#define NUM 1
#define SYM 2
#define ADJT 3
#define BLT 4



//Kolla upp mod type och repeating https://www.youtube.com/watch?v=NAUxTR4vGys

/ {

  // Activate ADJUST layer by pressing SYM and NUM
    conditional_layers {
        compatible = "zmk,conditional-layers";
        ADJT_layer {
            if-layers = <NUM SYM>;
            then-layer = <ADJT>;
        };
    };

  keymap {
    compatible = "zmk,keymap";

    default_layer {
// -----------------------------------------------------------------------------------------
            // |  ESC |  Q  |  W  |  E  |  R  |  T  |   |  Y  |  U   |  I  |  O  |  P  | DEL |
            // | CTRL |  A  |  S  |  D  |  F  |  G  |   |  H  |  J   |  K  |  L  |  Ö  |  Ä  |
            //        |  Z  |  X  |  C  |  V  |  B  |   |  N  |  M   |  ,  |  .  |  -  |
            //              | SHFT| GUI | NUM | SPC |   | BKSP| ENT  | SYM | ALT |

      bindings = <
        &lt SYM ESC   &kp Q &kp W &kp E     &kp R    &kp T                    &kp Y     &kp U    &kp I     &kp O   &kp P    &kp BSPC 
        &mt LCTRL TAB &kp A &kp S &kp D     &kp F    &kp G                    &kp H     &kp J    &kp K     &kp L   &kp SEMI &kp ENTER
                      &kp Z &kp X &kp C     &kp V    &kp B                    &kp N     &kp M    &kp COMMA &kp DOT &kp FSLH
                            &kp ENTER   &kp LGUI  &mo NUM  &kp LSHFT     &kp SPACE &mo SYM  &kp BSPC  &kp LALT
      >;
    };
    numbers {
      bindings = <
        &kp GRAVE &kp SV_TILDE &kp KP_PLUS &kp FSLH &kp SV_EQUAL &kp SV_CARET   &kp KP_MULTIPLY  &kp N7    &kp N8    &kp N9    &kp SV_PRCNT  &kp BSPC 
        &mt LCTRL TAB  &kp LGUI    &kp LALT  &kp LCTRL &kp LSHFT  &kp SV_HASH    &kp N0        &kp N1    &kp N2    &kp N3     &kp DOT  &kp ENTER 
                 &kp SV_PIPE &kp SV_LT &kp SV_GT &trans &kp SV_DQT         &kp KP_DIVIDE  &kp N4    &kp N5    &kp N6    &kp SV_DOLLAR
                                       &trans &trans &trans &trans         &kp SPACE     &trans   &trans   &trans

      >;
    };
    symbols {
      bindings = <
      // kp equal here not in use and tilde2 is already in use in num layer as multiply
        &lt SYM ESC    &kp EXCL    &kp SV_LT    &kp SV_LBKT  &kp SV_RBKT   &kp SV_GT               &kp HOME    &kp PG_DN  &kp PG_UP  &kp END   &kp EQUAL  &kp C_VOLUME_UP 
        &mt LCTRL TAB  &kp SV_SQT  &kp SV_UNDER &kp SV_LPAR  &kp SV_RPAR  &kp SV_AMPS              &kp LEFT    &kp DOWN   &kp UP     &kp RIGHT &kp ENTER  &kp C_VOLUME_DOWN 
                    &kp SV_BSLH &kp SV_AT    &kp SV_LBRC  &kp SV_RBRC  &kp SV_PIPE              &kp ESC     &kp BSPC   &kp DEL    &kp TAB   &kp TILDE2
                                       &trans &trans &trans &trans                    &trans &trans &trans &trans
      >;
    };
    adjust {
      bindings = <
            &trans     &trans  &trans &kp SV_A_UMLAUT  &kp NUMBER_7   &kp NUMBER_8             &kp T &kp N  &kp KP_DIVIDE  &kp SV_O_UMLAUT &kp KP_MINUS &kp C_PP 
            &mo BLT  &kp LBKT  &kp SV_A_UMLAUT &kp SV_O_UMLAUT &kp LSHFT &trans                &kp TAB &kp D &kp LALT     &kp LCTRL &kp LGUI        &kp C_NEXT
                      &kp SV_UMLAUT &kp SV_EURO &kp SV_ACUTE &kp SV_GRAVE  &kp PRINTSCREEN                       &kp N      &kp NUMBER_4 &kp NUMBER_5   &kp NUMBER_6    &kp RETURN      
                              &trans &trans &trans &trans                                       &trans       &trans       &trans         &trans 
                  
      >;
    };
    bluetooth {
      bindings = <
                &trans &ext_power EXT_POWER_TOGGLE_CMD &trans &trans &trans &trans     &bt BT_CLR  &trans   &trans    &kp MINUS &kp EQUAL   &bt BT_CLR 
                &trans &trans &trans &trans &trans &bt BT_PRV                          &bt BT_NXT   &bt BT_SEL 0  &bt BT_SEL 1    &trans    &trans      &bt BT_NXT
                          &trans &trans &trans &trans &kp LBKT                            &kp RBKT &trans   &kp C_PREV  &kp C_NEXT &ext_power EXT_POWER_TOGGLE_CMD 
                                              &trans &trans &trans &trans        &trans  &trans   &trans &trans
      >;
    };
  };
};        