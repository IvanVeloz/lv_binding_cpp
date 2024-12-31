/*
 * example.hpp
 *
 *  Created on: Aug 6, 2021
 *      Author: fstuffdev
 */

#ifndef EXAMPLE_HPP_
#define EXAMPLE_HPP_

#include "../lv_cpp/core/lvglpp.h"

#if defined(CONFIG_EXAMPLE_HELLO)
#include "HelloEx.h"
#endif

#if defined(CONFIG_EXAMPLE_FLEX)
#include "FlexEx.h"
#endif

#endif /* EXAMPLE_HPP_ */
