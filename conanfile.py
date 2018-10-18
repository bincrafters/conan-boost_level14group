#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires, tools


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostLevel14GroupConan(base.BoostBaseConan):
    # This is now Level 18
    name = "boost_level14group"
    url = "https://github.com/bincrafters/conan-boost_level14group"
    lib_short_names = [ "bimap", "disjoint_sets", "property_map", "graph"]
    header_only_libs = ["bimap", "disjoint_sets", "property_map"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    b2_requires = [
        "boost_algorithm",
        "boost_any",
        "boost_array",
        "boost_assert",
        "boost_bind",
        "boost_concept_check",
        "boost_config",
        "boost_container_hash",
        "boost_conversion",
        "boost_core",
        "boost_detail",
        "boost_dynamic_bitset",
        "boost_filesystem",
        "boost_foreach",
        "boost_function",
        "boost_integer",
        "boost_iterator",
        "boost_lambda",
        "boost_lexical_cast",
        "boost_math",
        "boost_move",
        "boost_mpl",
        "boost_multi_index",
        "boost_optional",
        "boost_parameter",
        "boost_preprocessor",
        "boost_property_tree",
        "boost_python",
        "boost_random",
        "boost_range",
        "boost_serialization",
        "boost_smart_ptr",
        "boost_spirit",
        "boost_static_assert",
        "boost_test",
        "boost_throw_exception",
        "boost_tti",
        "boost_tuple",
        "boost_type_traits",
        "boost_typeof",
        "boost_unordered",
        "boost_utility",
        "boost_variant",
        "boost_xpressive"
    ]


    def build_requirements_additional(self):
        if not tools.os_info.is_windows:
            self.build_requires("openmpi/3.0.0@bincrafters/stable")

    def package_info_additional(self):
        self.info.options["boost_python"].python_version = "any"