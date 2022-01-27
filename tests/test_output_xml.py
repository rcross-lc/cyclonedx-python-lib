# encoding: utf-8

# This file is part of CycloneDX Python Lib
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) OWASP Foundation. All Rights Reserved.
from os.path import dirname, join
from unittest.mock import Mock, patch

from cyclonedx.model.bom import Bom
from cyclonedx.output import get_instance, SchemaVersion
from data import get_bom_with_component_setuptools_basic, get_bom_with_component_setuptools_with_cpe, \
    get_bom_with_component_toml_1, get_bom_with_component_setuptools_no_component_version, \
    get_bom_with_component_setuptools_with_release_notes, get_bom_with_component_setuptools_with_vulnerability, \
    MOCK_UUID_1, MOCK_UUID_4, MOCK_UUID_5, MOCK_UUID_6, get_bom_just_complete_metadata
from tests.base import BaseXmlTestCase


class TestOutputXml(BaseXmlTestCase):

    def test_simple_bom_v1_4(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_basic(), schema_version=SchemaVersion.V1_4,
            fixture='bom_setuptools.xml'
        )

    def test_simple_bom_v1_3(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_basic(), schema_version=SchemaVersion.V1_3,
            fixture='bom_setuptools.xml'
        )

    def test_simple_bom_v1_2(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_basic(), schema_version=SchemaVersion.V1_2,
            fixture='bom_setuptools.xml'
        )

    def test_simple_bom_v1_1(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_basic(), schema_version=SchemaVersion.V1_1,
            fixture='bom_setuptools.xml'
        )

    def test_simple_bom_v1_0(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_basic(), schema_version=SchemaVersion.V1_0,
            fixture='bom_setuptools.xml'
        )

    def test_simple_bom_v1_4_with_cpe(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_with_cpe(), schema_version=SchemaVersion.V1_4,
            fixture='bom_setuptools_with_cpe.xml'
        )

    def test_simple_bom_v1_3_with_cpe(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_with_cpe(), schema_version=SchemaVersion.V1_3,
            fixture='bom_setuptools_with_cpe.xml'
        )

    def test_simple_bom_v1_2_with_cpe(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_with_cpe(), schema_version=SchemaVersion.V1_2,
            fixture='bom_setuptools_with_cpe.xml'
        )

    def test_simple_bom_v1_1_with_cpe(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_with_cpe(), schema_version=SchemaVersion.V1_1,
            fixture='bom_setuptools_with_cpe.xml'
        )

    def test_simple_bom_v1_0_with_cpe(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_with_cpe(), schema_version=SchemaVersion.V1_0,
            fixture='bom_setuptools_with_cpe.xml'
        )

    def test_bom_v1_4_component_hashes_external_references(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_toml_1(), schema_version=SchemaVersion.V1_4,
            fixture='bom_toml_hashes_and_references.xml'
        )

    def test_bom_v1_3_component_hashes_external_references(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_toml_1(), schema_version=SchemaVersion.V1_3,
            fixture='bom_toml_hashes_and_references.xml'
        )

    def test_bom_v1_2_component_hashes_external_references(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_toml_1(), schema_version=SchemaVersion.V1_2,
            fixture='bom_toml_hashes_and_references.xml'
        )

    def test_bom_v1_1_component_hashes_external_references(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_toml_1(), schema_version=SchemaVersion.V1_1,
            fixture='bom_toml_hashes_and_references.xml'
        )

    def test_bom_v1_0_component_hashes_external_references(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_toml_1(), schema_version=SchemaVersion.V1_0,
            fixture='bom_toml_hashes_and_references.xml'
        )

    def test_bom_v1_4_no_component_version(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_no_component_version(), schema_version=SchemaVersion.V1_4,
            fixture='bom_setuptools_no_version.xml'
        )

    def test_bom_v1_3_no_component_version(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_no_component_version(), schema_version=SchemaVersion.V1_3,
            fixture='bom_setuptools_no_version.xml'
        )

    def test_bom_v1_2_no_component_version(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_no_component_version(), schema_version=SchemaVersion.V1_2,
            fixture='bom_setuptools_no_version.xml'
        )

    def test_bom_v1_1_no_component_version(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_no_component_version(), schema_version=SchemaVersion.V1_1,
            fixture='bom_setuptools_no_version.xml'
        )

    def test_bom_v1_0_no_component_version(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_no_component_version(), schema_version=SchemaVersion.V1_0,
            fixture='bom_setuptools_no_version.xml'
        )

    def test_bom_v1_4_component_with_release_notes(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_with_release_notes(), schema_version=SchemaVersion.V1_4,
            fixture='bom_setuptools_with_release_notes.xml'
        )

    def test_bom_v1_3_component_with_release_notes(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_with_release_notes(), schema_version=SchemaVersion.V1_3,
            fixture='bom_setuptools.xml'
        )

    def test_bom_v1_4_component_with_vulnerability(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_with_vulnerability(), schema_version=SchemaVersion.V1_4,
            fixture='bom_setuptools_with_vulnerabilities.xml'
        )

    def test_bom_v1_3_component_with_vulnerability(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_with_vulnerability(), schema_version=SchemaVersion.V1_3,
            fixture='bom_setuptools_with_vulnerabilities.xml'
        )

    def test_bom_v1_2_component_with_vulnerability(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_with_vulnerability(), schema_version=SchemaVersion.V1_2,
            fixture='bom_setuptools_with_vulnerabilities.xml'
        )

    def test_bom_v1_1_component_with_vulnerability(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_with_vulnerability(), schema_version=SchemaVersion.V1_1,
            fixture='bom_setuptools_with_vulnerabilities.xml'
        )

    def test_bom_v1_0_component_with_vulnerability(self) -> None:
        self._validate_xml_bom(
            bom=get_bom_with_component_setuptools_with_vulnerability(), schema_version=SchemaVersion.V1_0,
            fixture='bom_setuptools.xml'
        )

    @patch('cyclonedx.model.component.uuid4', return_value=MOCK_UUID_6)
    def test_bom_v1_4_with_metadata_component(self, mock_uuid: Mock) -> None:
        self._validate_xml_bom(
            bom=get_bom_just_complete_metadata(), schema_version=SchemaVersion.V1_4,
            fixture='bom_with_full_metadata.xml'
        )
        mock_uuid.assert_called()

    @patch('cyclonedx.model.component.uuid4', return_value=MOCK_UUID_5)
    def test_bom_v1_3_with_metadata_component(self, mock_uuid: Mock) -> None:
        self._validate_xml_bom(
            bom=get_bom_just_complete_metadata(), schema_version=SchemaVersion.V1_3,
            fixture='bom_with_full_metadata.xml'
        )
        mock_uuid.assert_called()

    @patch('cyclonedx.model.component.uuid4', return_value=MOCK_UUID_4)
    def test_bom_v1_2_with_metadata_component(self, mock_uuid: Mock) -> None:
        self._validate_xml_bom(
            bom=get_bom_just_complete_metadata(), schema_version=SchemaVersion.V1_2,
            fixture='bom_with_full_metadata.xml'
        )
        mock_uuid.assert_called()

    @patch('cyclonedx.model.component.uuid4', return_value=MOCK_UUID_1)
    def test_bom_v1_1_with_metadata_component(self, mock_uuid: Mock) -> None:
        self._validate_xml_bom(
            bom=get_bom_just_complete_metadata(), schema_version=SchemaVersion.V1_1,
            fixture='bom_empty.xml'
        )
        mock_uuid.assert_called()

    @patch('cyclonedx.model.component.uuid4', return_value=MOCK_UUID_1)
    def test_bom_v1_0_with_metadata_component(self, mock_uuid: Mock) -> None:
        self._validate_xml_bom(
            bom=get_bom_just_complete_metadata(), schema_version=SchemaVersion.V1_0,
            fixture='bom_empty.xml'
        )
        mock_uuid.assert_called()

    # Helper methods
    def _validate_xml_bom(self, bom: Bom, schema_version: SchemaVersion, fixture: str) -> None:
        outputter = get_instance(bom=bom, schema_version=schema_version)
        self.assertEqual(outputter.schema_version, schema_version)
        with open(
                join(dirname(__file__), f'fixtures/xml/{schema_version.to_version()}/{fixture}')) as expected_xml:
            self.assertValidAgainstSchema(bom_xml=outputter.output_as_string(), schema_version=schema_version)
            self.assertEqualXmlBom(
                expected_xml.read(), outputter.output_as_string(), namespace=outputter.get_target_namespace()
            )
            expected_xml.close()
